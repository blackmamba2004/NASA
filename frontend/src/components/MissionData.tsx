import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import qs from 'qs';
import FiltersComponent from './Filters';
import PaginatorComponent from './Paginator';
import { MissionDataResponse } from '../types/mission';
import { Filters } from '../types/filters';
import '../css/MissionData.css';

const MissionData: React.FC = () => {
  const [data, setData] = useState<MissionDataResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [filters, setFilters] = useState<Filters>({
    rover_name: '',
    sol_from: null,
    sol_to: null,
    earth_date_from: null,
    earth_date_to: null,
    min_total_photo: null,
    max_total_photo: null,
    cameras: [],
    page: 1,
    size: 30,
  });

  const paramsSerializer = (params: any) => {
    const { cameras, ...rest } = params;
    const camerasQuery = qs.stringify({ cameras }, { arrayFormat: 'repeat' });
    const restQuery = qs.stringify(rest, { skipNulls: true });
    return [restQuery, camerasQuery].filter(Boolean).join('&');
  };

  const fetchData = useCallback(async () => {
    if (filters.rover_name === '') {
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get<MissionDataResponse>(
        'http://127.0.0.1:8000/nasa/mission',
        {
          params: { ...filters },
          paramsSerializer,
        }
      );
      setData(response.data);
    } catch (error) {
      console.error('Error fetching mission data:', error);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleFilterChange = (key: keyof Filters, value: any) => {
    setFilters((prevFilters) => ({
      ...prevFilters,
      [key]: value,
      page: 1,
    }));
  };

  const handlePageChange = (newPage: number) => {
    setFilters((prevFilters) => ({
      ...prevFilters,
      page: newPage,
    }));
  };

  const renderData = () => {
    if (loading) return <div>Загрузка...</div>;
    if (!data) return <div>Выберите ровер, чтобы увидеть данные миссии</div>;

    const manifest = data.data.photo_manifest;

    return (
      <div>
        <h3>Миссия ровера {manifest.name} </h3>
        <p>🟢 Статус: {manifest.status}</p>
        <p>🚀 Запуск: {manifest.launch_date}</p>
        <p>🛬 Посадка: {manifest.landing_date}</p>
        <p>📆 Максимальная земная дата: {manifest.max_date}</p>
        <p>📸 Всего фото: {manifest.total_photos}</p>

        <div className="card-container">
          {manifest.sol_activities.map((activity) => (
            <div className="card" key={activity.sol}>
              <div className="card-header">
                <strong>Марсианский день {activity.sol}:</strong>
              </div>
              <div className="card-body">
                <p>Фото: {activity.total_photos}</p>
                <p>📅 Земная дата: {activity.earth_date}</p>
                <p>📷 Камеры: {activity.cameras.join(', ')}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div>
      <FiltersComponent filters={filters} onChange={handleFilterChange} />
      {renderData()}
      {data && <PaginatorComponent paginator={data.paginator} onPageChange={handlePageChange} />}
    </div>
  );
};

export default MissionData;

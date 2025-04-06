import React from 'react';
import { RoverNameEnum, RoverCameraEnum } from '../types/mission';
import { Filters } from '../types/filters';
import '../css/Filters.css'

interface FiltersProps {
  filters: Filters;
  onChange: (key: keyof Filters, value: any) => void;
}

const FiltersComponent: React.FC<FiltersProps> = ({ filters, onChange }) => {
  const handleFilterChange = (key: keyof Filters, value: any) => {
    onChange(key, value);
  };

  return (
    <div className="filters-container">
      <div className="filter-group">
        <label>Ровер</label>
        <select
          value={filters.rover_name}
          onChange={(e) => handleFilterChange('rover_name', e.target.value)}
        >
          <option value="">Выберите ровер</option>
          {Object.values(RoverNameEnum).map((rover) => (
            <option key={rover} value={rover}>
              {rover}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label>Мин. марсианский день (Sol)</label>
        <input
          type="number"
          value={filters.sol_from || ''}
          onChange={(e) =>
            handleFilterChange('sol_from', e.target.value ? parseInt(e.target.value, 10) : null)
          }
        />
      </div>

      <div className="filter-group">
        <label>Макс. марсианский день (Sol)</label>
        <input
          type="number"
          value={filters.sol_to || ''}
          onChange={(e) =>
            handleFilterChange('sol_to', e.target.value ? parseInt(e.target.value, 10) : null)
          }
        />
      </div>

      <div className="filter-group">
        <label>Дата с (Земля)</label>
        <input
          type="date"
          value={filters.earth_date_from || ''}
          onChange={(e) => handleFilterChange('earth_date_from', e.target.value || null)}
        />
      </div>

      <div className="filter-group">
        <label>Дата по (Земля)</label>
        <input
          type="date"
          value={filters.earth_date_to || ''}
          onChange={(e) => handleFilterChange('earth_date_to', e.target.value || null)}
        />
      </div>

      <div className="filter-group">
        <label>Мин. количество фото</label>
        <input
          type="number"
          value={filters.min_total_photo || ''}
          onChange={(e) =>
            handleFilterChange(
              'min_total_photo',
              e.target.value ? parseInt(e.target.value, 10) : null
            )
          }
        />
      </div>

      <div className="filter-group">
        <label>Макс. количество фото</label>
        <input
          type="number"
          value={filters.max_total_photo || ''}
          onChange={(e) =>
            handleFilterChange(
              'max_total_photo',
              e.target.value ? parseInt(e.target.value, 10) : null
            )
          }
        />
      </div>

      <div className="filter-group">
        <label>Камеры</label>
        <select
          multiple
          value={filters.cameras}
          onChange={(e) =>
            handleFilterChange(
              'cameras',
              Array.from(e.target.selectedOptions, (option) => option.value as RoverCameraEnum)
            )
          }
        >
          {Object.values(RoverCameraEnum).map((camera) => (
            <option key={camera} value={camera}>
              {camera}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default FiltersComponent;
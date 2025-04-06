import React from 'react';
import { Paginator } from '../types/mission';
import '../css/Paginator.css'; // Подключаем CSS файл

interface PaginatorProps {
  paginator: Paginator;
  onPageChange: (newPage: number) => void;
}

const PaginatorComponent: React.FC<PaginatorProps> = ({ paginator, onPageChange }) => {
  return (
    <div className="paginator">
      <button
        className={`paginator-btn ${!paginator.has_prev ? 'disabled' : ''}`}
        onClick={() => onPageChange(paginator.page - 1)}
        disabled={!paginator.has_prev}
      >
        &#8592; Prev
      </button>

      <span className="paginator-page-info">
        Page {paginator.page} of {paginator.total}
      </span>

      <button
        className={`paginator-btn ${!paginator.has_next ? 'disabled' : ''}`}
        onClick={() => onPageChange(paginator.page + 1)}
        disabled={!paginator.has_next}
      >
        Next &#8594;
      </button>
    </div>
  );
};

export default PaginatorComponent;

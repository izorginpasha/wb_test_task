import React from "react";

const FilterPanel = ({ filters, setFilters }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">Название товара</label>
        <input
          type="text"
          name="name"
          value={filters.name}
          onChange={handleChange}
          className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Минимальная цена</label>
        <input
          type="number"
          name="min_price"
          value={filters.min_price}
          onChange={handleChange}
          className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Максимальная цена</label>
        <input
          type="number"
          name="max_price"
          value={filters.max_price}
          onChange={handleChange}
          className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Минимальный рейтинг</label>
        <input
          type="number"
          step="0.1"
          name="min_rating"
          value={filters.min_rating}
          onChange={handleChange}
          className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Минимум отзывов</label>
        <input
          type="number"
          name="min_feedbacks"
          value={filters.min_feedbacks}
          onChange={handleChange}
          className="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
        />
      </div>
    </div>
  );
};

export default FilterPanel;

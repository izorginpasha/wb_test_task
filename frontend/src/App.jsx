import React, { useState } from "react";
import FilterPanel from "./Filters";
import ProductTable from "./ProductTable";
import Charts from "./Charts";
import { fetchProducts } from "./api/products";

const App = () => {
  const [filters, setFilters] = useState({
    min_price: 0,
    max_price: 100000,
    min_rating: 0,
    min_feedbacks: 0,
    name: ""
  });

  const [products, setProducts] = useState([]);

  const handleApplyFilters = async () => {
    try {
      const data = await fetchProducts(filters);
      setProducts(data);
    } catch (error) {
      console.error("Ошибка загрузки продуктов:", error);
    }
  };

  return (
    <div className="p-4 space-y-6">
      <h1 className="text-3xl font-bold mb-4">Аналитика Wildberries</h1>
      <FilterPanel filters={filters} setFilters={setFilters} />
      <button
        onClick={handleApplyFilters}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
      >
        Применить фильтры
      </button>
      <ProductTable products={products} />
      <Charts products={products} />
    </div>
  );
};

export default App;

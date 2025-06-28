import React from "react";

const ProductTable = ({ products }) => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-4 py-2 border">Название</th>
            <th className="px-4 py-2 border">Цена</th>
            <th className="px-4 py-2 border">Цена со скидкой</th>
            <th className="px-4 py-2 border">Рейтинг</th>
            <th className="px-4 py-2 border">Отзывы</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p, i) => (
            <tr key={i} className="text-center">
              <td className="border px-4 py-2">{p.name}</td>
              <td className="border px-4 py-2">{p.price}</td>
              <td className="border px-4 py-2">{p.sale_price}</td>
              <td className="border px-4 py-2">{p.rating}</td>
              <td className="border px-4 py-2">{p.feedbacks}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductTable;
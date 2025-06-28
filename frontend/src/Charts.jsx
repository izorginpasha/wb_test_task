import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from "recharts";

const Charts = ({ products }) => {
  const priceBuckets = [
    { range: "0-1000", count: 0 },
    { range: "1000-3000", count: 0 },
    { range: "3000-5000", count: 0 },
    { range: "5000-10000", count: 0 },
    { range: "10000+", count: 0 }
  ];

  const discountVsRating = [];

  products.forEach((p) => {
    const price = p.price;
    if (price < 1000) priceBuckets[0].count++;
    else if (price < 3000) priceBuckets[1].count++;
    else if (price < 5000) priceBuckets[2].count++;
    else if (price < 10000) priceBuckets[3].count++;
    else priceBuckets[4].count++;

    discountVsRating.push({
      rating: p.rating,
      discount: p.price - p.sale_price
    });
  });

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
      <div>
        <h2 className="text-lg font-semibold">Гистограмма цен</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={priceBuckets}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="range" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div>
        <h2 className="text-lg font-semibold">Скидка vs Рейтинг</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={discountVsRating}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="rating" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="discount" stroke="#82ca9d" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default Charts;
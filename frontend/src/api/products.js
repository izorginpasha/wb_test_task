
export const fetchProducts = async (filters) => {
  const params = new URLSearchParams(filters).toString();
  const response = await fetch(`/api/products/?${params}`);
  if (!response.ok) {
    throw new Error("Ошибка при загрузке продуктов");
  }
  return await response.json();
};
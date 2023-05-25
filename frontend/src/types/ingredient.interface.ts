// export interface Ingredient {
//   id: number;
//   user_id: number;
//   title: string;
//   slug: string;
//   summary: string;
//   type: string;
//   quantity: string;
//   createdAt: string;
//   updatedAt: string;
//   content: string;
// }

export interface Ingredient {
  id: number;
  account_id: number;
  title: string;
  description: string;
  sku: string;
  createdAt: string;
  updatedAt: string;
  ingredientInfo: IngredientInfo[];
}

export interface IngredientInfo {
  id: number;
  account_id: number;
  ingredient_id: number;
  slug: string;
  quantity: number;
  unit: string;
  purchase_price: number;
  purchase_date: string;
  expiration_date: string;
  createdAt: string;
  updatedAt: string;
}

import api from '@/plguins/axios';
import AsyncStorage from '@react-native-community/async-storage';
const ENDPOINTS = {
  LOGIN: '/api/v1/auth/login',
  SIGNUP: '/api/v1/auth/register',
  LOGOUT: '/api/v1/auth/logout',
};

class IngredientService {
  async init() {
    const token = await this.getToken();
    const user = await this.getUser();
    if (token && user) {
      await this.setAuthorizationHeader(token);
    }
  }

  async setAuthorizationHeader(token) {
    api.defaults.headers.common['Authorization'] = `Token ${token}`;
  }
  async getToken() {
    const token = await this.getUser();
    return token.access_token;
  }

  async getUser() {
    const user = await AsyncStorage.getItem('user');

    return JSON.parse(user);
  }
  async get(ingredientId: number) {
    try {
      const { data } = await api.get(`api/v1/ingredients/${ingredientId}`);
      return data;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async getAll() {
    try {
      const { data } = await api.get('/api/v1/ingredients/');
      return data.ingredients;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async create(data) {
    try {
      console.log(data);
      const ingredient = await api.post('api/v1/ingredients/', data);
      return ingredient.data;
    } catch (error) {
      console.log(error);
    }
  }
  async delete(ingredientId) {
    try {
      await api.delete(`api/v1/ingredients/${ingredientId}/`);
      return true;
    } catch (error) {
      console.log(error);
    }
  }
  async updateQuantity(ingredientId: number, data: object) {
    return null;
  }
  async add_to_recipe(recipeId: number, ingredientId: number, data: object) {
    try {
      await api.post(
        `/api/v1/recipe-ingredient/${recipeId}/ingredient/${ingredientId}`,
        data
      );
    } catch (err) {
      console.log(err);
    }
  }
}
const ingredientService = new IngredientService();
ingredientService.init();
export default ingredientService;

import api from '@/plguins/axios';
import AsyncStorage from '@react-native-community/async-storage';
const ENDPOINTS = {
  LOGIN: '/api/v1/auth/login',
  SIGNUP: '/api/v1/auth/register',
  LOGOUT: '/api/v1/auth/logout',
};

class RecipeService {
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
  async getAll() {
    try {
      const { data } = await api.get('/api/v1/recipes/');
      return data.recipes;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async create(recipeData) {
    try {
      const { data } = await api.post('/api/v1/recipes/', recipeData);
      return data;
    } catch (err) {
      console.log(err);
    }
  }
  async get(recipeId: number) {
    try {
      const { data } = await api.get(`api/v1/recipes/${recipeId}`);
      return data;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async get_ingredients(recipeId: number) {
    try {
      const { data } = await api.get(`api/v1/recipes/${recipeId}/ingredients`);
      return data;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async delete(recipeId) {
    try {
      await api.get(`api/v1/recipes/${recipeId}`);
      return true;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
}

const recipeService = new RecipeService();
recipeService.init();
export default recipeService;

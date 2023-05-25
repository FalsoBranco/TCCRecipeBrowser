import api from '@/plguins/axios';
import AsyncStorage from '@react-native-community/async-storage';
import { AxiosError } from 'axios';

const ENDPOINTS = {
  LOGIN: '/api/v1/auth/login',
  SIGNUP: '/api/v1/auth/register',
  LOGOUT: '/api/v1/auth/logout',
};

class AuthServices {
  async login(userInfo) {
    try {
      const { data } = await api.post('/api/v1/auth/login', userInfo);
      api.defaults.headers.common[
        'Authorization'
      ] = `Token ${data.access_token}`;
      return data;
    } catch (error) {
      console.log(error);
      alert('Error: ' + error.response.data.detail);
    }
  }
  async logout(navigation) {
    try {
      await AsyncStorage.removeItem('user'); //Removing the token from local storage while logging out
      navigation.reset({ routes: [{ name: 'Preload' }] });
    } catch (err) {
      console.log(err);
    }
  }
}

export default new AuthServices();

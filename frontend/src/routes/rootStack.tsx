import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import Preload from '@/screens/Preload';
import SignIn from '@/screens/SignIn';
import MainAppDrawer from './mainAppDrawer';
import IngredientDetail from '@/screens/IngredientDetail';
import IngredientCreate from '@/screens/IngredientCreate';
const { Screen, Navigator } = createStackNavigator();
const RootStack = () => {
  return (
    <Navigator
      screenOptions={{ headerShown: false }}
      initialRouteName="Preload"
    >
      <Screen name="Preload" component={Preload} />
      <Screen name="SignIn" component={SignIn} />
      <Screen name="MainApp" component={MainAppDrawer} />
      <Screen name="DetailIngredient" component={IngredientDetail} />
      <Screen name="CreateIngredient" component={IngredientCreate} />
    </Navigator>
  );
};

export default RootStack;

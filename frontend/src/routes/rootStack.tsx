import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import Preload from '@/screens/Preload';
import SignIn from '@/screens/SignIn';
import MainAppDrawer from './mainAppDrawer';
import IngredientDetail from '@/screens/IngredientDetail';
import IngredientCreate from '@/screens/IngredientCreate';
import RecipeCreate from '@/screens/RecipeCreate';
import RecipeDetail from '@/screens/RecipeDetail';
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
      <Screen
        name="DetailIngredient"
        component={IngredientDetail}
        options={{
          headerShown: true,
        }}
      />
      <Screen name="DetailRecipe" component={RecipeDetail} />
      <Screen name="CreateIngredient" component={IngredientCreate} />
      <Screen name="CreateRecipe" component={RecipeCreate} />
    </Navigator>
  );
};

export default RootStack;

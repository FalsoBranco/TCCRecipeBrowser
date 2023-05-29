import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import Preload from '@/screens/Preload';
import SignIn from '@/screens/SignIn';
import MainAppDrawer from './mainAppDrawer';
import IngredientDetail from '@/screens/IngredientDetail';
import IngredientCreate from '@/screens/IngredientCreate';
import RecipeCreate from '@/screens/RecipeCreate';
import RecipeDetail from '@/screens/RecipeDetail';
import AddRecipeIngredient from '@/screens/AddRecipeIngredient';
const { Screen, Navigator, Group } = createStackNavigator();
const RootStack = () => {
  return (
    <Navigator
      screenOptions={{ headerShown: false }}
      initialRouteName="Preload"
    >
      <Screen name="Preload" component={Preload} />
      <Screen name="SignIn" component={SignIn} />
      <Screen name="MainApp" component={MainAppDrawer} />
      <Group
        screenOptions={{
          headerShown: true,
        }}
      >
        <Screen name="DetailIngredient" component={IngredientDetail} />
        <Screen name="DetailRecipe" component={RecipeDetail} />
      </Group>
      <Group>
        <Screen name="CreateIngredient" component={IngredientCreate} />
        <Screen name="CreateRecipe" component={RecipeCreate} />
      </Group>
      <Group screenOptions={{ presentation: 'modal' }}>
        <Screen name="AddRecipeIngredient" component={AddRecipeIngredient} />
      </Group>
    </Navigator>
  );
};

export default RootStack;

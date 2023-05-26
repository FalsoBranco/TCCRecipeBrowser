import { View, Text, ScrollView, HStack, VStack } from 'native-base';
import React, { useEffect, useState } from 'react';
import { useRoute } from '@react-navigation/native';
import recipeService from '@/services/RecipeService';

const RecipeDetail = () => {
  const [recipe, setRecipe] = useState();
  const route = useRoute();

  useEffect(() => {
    async function fetchRecipe() {
      const itemId = route.params.params.itemId;
      const recipeData = await recipeService.get(itemId);
      setRecipe(recipeData.recipe);
    }
    fetchRecipe();
  }, []);
  if (!recipe) {
    return null;
  }
  console.log(route);
  return (
    <View>
      <VStack>
        <Text>{JSON.stringify(recipe)}</Text>

        <ScrollView
          borderRadius={8}
          borderColor={'black'}
          borderWidth={2}
          m={4}
          h="32"
        >
          <Text m={1}>{recipe.title}</Text>
        </ScrollView>
      </VStack>
    </View>
  );
};

export default RecipeDetail;

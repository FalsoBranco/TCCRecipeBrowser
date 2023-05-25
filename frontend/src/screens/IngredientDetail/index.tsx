import { View, Text, ScrollView, HStack, VStack } from 'native-base';
import React, { useEffect, useState } from 'react';
import { useRoute } from '@react-navigation/native';
import ingredientService from '@/services/IngredientService';

const IngredientDetail = () => {
  const [ingredient, setIngredient] = useState();
  const route = useRoute();

  useEffect(() => {
    async function fetchIngredient() {
      const itemId = route.params.params.itemId;
      const ingredientData = await ingredientService.get(itemId);
      setIngredient(ingredientData.ingredient);
    }
    fetchIngredient();
  }, []);
  if (!ingredient) {
    return null;
  }
  console.log(route);
  return (
    <View>
      <VStack>
        <Text>{JSON.stringify(ingredient)}</Text>

        <ScrollView
          borderRadius={8}
          borderColor={'black'}
          borderWidth={2}
          m={4}
          h="32"
        >
          <Text m={1}>{ingredient.title}</Text>
        </ScrollView>
      </VStack>
    </View>
  );
};

export default IngredientDetail;

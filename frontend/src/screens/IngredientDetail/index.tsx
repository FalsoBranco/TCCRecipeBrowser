import {
  View,
  Text,
  HStack,
  VStack,
  Image,
  Heading,
  Box,
  ScrollView,
  Center,
  Pressable,
} from 'native-base';
import React, { useEffect, useState } from 'react';
import { useNavigation, useRoute } from '@react-navigation/native';
import ingredientService from '@/services/IngredientService';

const IngredientDetail = () => {
  const [ingredient, setIngredient] = useState();
  const route = useRoute();
  const navigation = useNavigation();

  useEffect(() => {
    async function fetchIngredient() {
      const itemId = route.params.params.itemId;
      const ingredientData = await ingredientService.get(itemId);
      setIngredient(ingredientData.ingredient);
      navigation.setOptions({ title: ingredientData.ingredient.title });
    }
    fetchIngredient();
  }, []);
  if (!ingredient) {
    return null;
  }
  return (
    <View m={4}>
      <VStack space={4}>
        <HStack>
          <Image
            flex={1}
            borderRadius={8}
            h={32}
            source={{
              uri: 'https://www.holidify.com/images/cmsuploads/compressed/Bangalore_citycover_20190613234056.jpg',
            }}
            alt="image"
          />
          <VStack space={2} pl={2} flex={2}>
            <Heading>{ingredient.title}</Heading>
            <Text>
              Validade:{' '}
              {new Date(ingredient.expired_date).toLocaleDateString('pt-BR')}
            </Text>
          </VStack>
        </HStack>
        <Center>
          <Text>Quantidade</Text>
          <HStack space={24}>
            <Pressable>
              <Text>+</Text>
            </Pressable>
            <Text>
              {ingredient.quantity} {ingredient.unit.unit}
            </Text>
            <Pressable>
              <Text>-</Text>
            </Pressable>
          </HStack>
        </Center>
        <ScrollView
          mt={8}
          borderColor={'black'}
          borderWidth={1}
          h={'48'}
          borderRadius={8}
          p={2}
        >
          <Text>{ingredient.summary}</Text>
        </ScrollView>
      </VStack>
    </View>
  );
};

export default IngredientDetail;

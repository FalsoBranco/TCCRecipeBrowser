import {
  View,
  Text,
  ScrollView,
  HStack,
  VStack,
  Image,
  Heading,
  Box,
  FlatList,
  Flex,
  Modal,
  Pressable,
  Button,
} from 'native-base';
import React, { useEffect, useState } from 'react';
import { useNavigation, useRoute } from '@react-navigation/native';
import recipeService from '@/services/RecipeService';
import Ionicons from '@expo/vector-icons/Ionicons';

const RecipeDetail = () => {
  const route = useRoute();
  const navigation = useNavigation();

  const [recipe, setRecipe] = useState({});
  const [recipeIngredients, setRecipeIngredients] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [modalVisible, setModalVisible] = useState(false);

  const portions = `${recipe?.amounts} porções`;

  async function handleDeleteRecipe() {
    const deleted = await recipeIngredients.delete(recipe.id);
    setModalVisible(false);
    if (deleted) {
      navigation.navigate('Recipes');
    } else {
      return;
    }
  }

  function configHeader(navigation, recipeData) {
    navigation.setOptions({
      title: recipeData.recipe.title,
      headerRight: () => (
        <Pressable mr={1}>
          <Ionicons
            name="trash-bin-outline"
            color="red"
            onPress={() => setModalVisible(!modalVisible)}
            size={32}
            ml={2}
          />
        </Pressable>
      ),
    });
  }
  useEffect(() => {
    async function fetchRecipe() {
      const itemId = route.params.params.itemId;
      const [recipeData, ingredientsData] = await Promise.all([
        recipeService.get(itemId),
        recipeService.get_ingredients(itemId),
      ]);
      setRecipe(recipeData.recipe);
      setRecipeIngredients(ingredientsData.recipe.ingredients);

      setIsLoading(false);
      configHeader(navigation, recipeData);
    }
    fetchRecipe();
  }, []);

  if (isLoading) {
    return null;
  }

  function handleAddIngredient() {
    navigation.navigate('AddRecipeIngredient', {
      recipeId: recipe.id,
    });
  }

  return (
    <>
      <ScrollView>
        <View m={4}>
          <VStack space={4}>
            <HStack>
              <Image
                flex={1}
                borderRadius={8}
                h={32}
                source={{
                  uri: 'https://placehold.co/400.png',
                }}
                alt="image"
              />
              <VStack space={2} pl={2} flex={2}>
                <Heading>{recipe.title}</Heading>
              </VStack>
            </HStack>
            <ScrollView
              mt={8}
              borderColor={'black'}
              borderWidth={1}
              h={'32'}
              borderRadius={8}
              p={2}
            >
              <Text>{recipe.summary}</Text>
            </ScrollView>
            <HStack
              justifyContent={'space-between'}
              p={2}
              borderWidth={1}
              borderColor={'black'}
              bgColor="#f3f3f3"
            >
              <Heading fontSize={'xl'}>Ingredientes ({portions})</Heading>
              <Ionicons
                onPress={handleAddIngredient}
                name="add-outline"
                size={24}
              />
            </HStack>
            {recipeIngredients.map((ingredient) => (
              <Text key={ingredient.ingredient.id}>
                {ingredient.ingredient.title}
              </Text>
            ))}
            {/* <FlatList
            data={recipeIngredients}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => <Text>{item.ingredient.title}</Text>}
          /> */}
            <Box p={2} borderWidth={1} borderColor={'black'} bgColor="#f3f3f3">
              <Heading fontSize={'xl'}>Instruções</Heading>
            </Box>
            <ScrollView
              mt={1}
              borderColor={'black'}
              borderWidth={1}
              h={'48'}
              borderRadius={8}
              p={2}
            >
              <Text>{recipe.instructions}</Text>
            </ScrollView>
          </VStack>
        </View>
      </ScrollView>
      <Modal
        size={'xl'}
        isOpen={modalVisible}
        onClose={() => setModalVisible(false)}
      >
        <Modal.Content>
          <Modal.Body>
            <VStack space={2} alignItems={'center'}>
              <Ionicons name="trash-outline" size={32} color={'#ac0909'} />
              <Heading size={'sm'}>
                Você está preste a deletar uma receita
              </Heading>
              <Box alignItems={'center'}>
                <Text fontWeight={'bold'} color={'#8d8d8d'}>
                  Isso ira deletar a receita
                </Text>
                <Text fontWeight={'bold'} color={'#8d8d8d'}>
                  Você tem certeza?
                </Text>
              </Box>
            </VStack>
            <Flex direction="row-reverse">
              <Button.Group space={2} m={2}>
                <Button
                  variant="ghost"
                  colorScheme="blueGray"
                  onPress={() => {
                    setModalVisible(false);
                  }}
                >
                  Cancelar
                </Button>
                <Button
                  colorScheme={'warning'}
                  onPress={() => {
                    handleDeleteRecipe();
                  }}
                >
                  Confirmar
                </Button>
              </Button.Group>
            </Flex>
          </Modal.Body>
        </Modal.Content>
      </Modal>
    </>
  );
};

export default RecipeDetail;

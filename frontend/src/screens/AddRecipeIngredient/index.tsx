import IngredientService from '@/services/IngredientService';
import { useEffect, useState } from 'react';
import { Box, FlatList, View, Text, Pressable, HStack } from 'native-base';
import { useNavigation, useRoute } from '@react-navigation/native';
import Ionicons from '@expo/vector-icons/Ionicons';

const AddRecipeIngredient = () => {
  const route = useRoute();
  const navigation = useNavigation();
  const recipeId = route.params.recipeId;

  const [data, setData] = useState();
  const [selectedItems, setSelectedItems] = useState([]);

  async function handleSelectedItem(id) {
    const objetoExistente = selectedItems.find(
      (objeto) => objeto.ingredientId === id
    );
    if (objetoExistente) {
      // Objeto já existe, incrementar a quantidade
      const novoArray = selectedItems.map((objeto) => {
        if (objeto.ingredientId === id) {
          return {
            ...objeto,
            quantity: objeto.quantity + 1,
          };
        }
        return objeto;
      });

      setSelectedItems(novoArray);
    } else {
      console.log(selectedItems);
      // Objeto não existe, adicionar ao array
      const novoObjeto = {
        ingredientId: id,
        quantity: 1,
      };

      setSelectedItems([...selectedItems, novoObjeto]);
    }
  }

  async function addToApi() {
    // if (selectedItems.length === 0) {
    //   navigation.navigate('DetailRecipe', { params: { itemId: recipeId } });
    //   return;
    // }
    selectedItems.forEach(async (ingredient) => {
      let extra = {
        extra: {
          quantity: ingredient.quantity,
          unittype_id: 0,
        },
      };
      console.log(ingredient, extra);
      await IngredientService.add_to_recipe(
        recipeId,
        ingredient.ingredientId,
        extra
      );
    });
  }

  async function loadIngredients() {
    const response = await IngredientService.getAll();
    if (!response) {
      return <View>Alo</View>;
    }
    setData(response);
  }

  function configHeader(navigation) {
    navigation.setOptions({
      title: 'Adicinando Ingredients',
      headerShown: true,
      headerRight: () => (
        <Pressable mr={1}>
          <Ionicons
            name="save-outline"
            color="green"
            onPress={() => addToApi()}
            size={32}
            ml={2}
          />
        </Pressable>
      ),
    });
  }

  const onRefreshing = () => {
    loadIngredients();
  };

  useEffect(() => {
    loadIngredients();
    configHeader(navigation);
  }, []);

  return (
    <Box safeArea flex="1">
      <FlatList
        showsVerticalScrollIndicator={false}
        flex={1}
        data={data}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View
            padding={4}
            m={2}
            borderWidth={1}
            borderRadius={8}
            borderColor={'black'}
            flex={1}
            flexDirection={'row'}
          >
            <HStack flex={1} justifyContent={'space-between'}>
              <Text>{item.title}</Text>
              <Pressable onPress={() => handleSelectedItem(item.id)}>
                <Text>Adicionar</Text>
              </Pressable>
            </HStack>
          </View>
        )}
      />
    </Box>
  );
};

export default AddRecipeIngredient;

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
  Input,
  Pressable,
  Modal,
  Button,
  Flex,
  FormControl,
} from 'native-base';
import React, { useEffect, useRef, useState } from 'react';
import { useNavigation, useRoute } from '@react-navigation/native';
import Ionicons from '@expo/vector-icons/Ionicons';

import ingredientService from '@/services/IngredientService';

const IngredientDetail = () => {
  const [ingredient, setIngredient] = useState();
  const [modalDeleteVisible, setModalDeleteVisible] = useState(false);
  const [modalQuantityVisible, setModalQuantityVisible] = useState(false);

  const newQuantity = useRef();

  const route = useRoute();
  const navigation = useNavigation();

  async function handleDeleteIngredient() {
    const deleted = await ingredientService.delete(ingredient.id);
    setModalDeleteVisible(false);
    if (deleted) {
      navigation.navigate('Ingredients');
    } else {
      return;
    }
  }
  async function handleUpdateQuantity() {
    await ingredientService.updateQuantity(ingredient.id, {
      quantity: ingredient.quantity,
    });
  }
  function configHeader(navigation, ingredientData) {
    navigation.setOptions({
      title: ingredientData.ingredient.title,
      headerRight: () => (
        <Pressable mr={1}>
          <Ionicons
            name="trash-bin-outline"
            color="red"
            onPress={() => setModalDeleteVisible(!modalDeleteVisible)}
            size={32}
          />
        </Pressable>
      ),
    });
  }

  useEffect(() => {
    async function fetchIngredient() {
      const itemId = route.params.params.itemId;
      const ingredientData = await ingredientService.get(itemId);
      setIngredient(ingredientData.ingredient);
      configHeader(navigation, ingredientData);
    }
    fetchIngredient();
  }, []);

  if (!ingredient) {
    return null;
  }
  return (
    <>
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
              <Heading>{ingredient.title}</Heading>
              <Text>
                Validade:{' '}
                {new Date(ingredient.expired_date).toLocaleDateString('pt-BR')}
              </Text>
            </VStack>
          </HStack>
          <Center>
            <Text>Quantidade</Text>
            <HStack space={24} alignItems={'center'}>
              <Pressable mr={1}>
                <Ionicons
                  name="add-outline"
                  color="red"
                  onPress={() => console.log('Add')}
                  size={32}
                />
              </Pressable>
              <Pressable onPress={() => setModalQuantityVisible(true)}>
                <Text>
                  {ingredient.quantity} {ingredient.unit.unit}
                </Text>
              </Pressable>
              <Pressable>
                <Ionicons
                  name="remove-outline"
                  color="red"
                  onPress={() => console.log('Remover')}
                  size={32}
                />
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
      <Modal
        size={'xl'}
        isOpen={modalDeleteVisible}
        onClose={() => setModalDeleteVisible(false)}
      >
        <Modal.Content>
          <Modal.Body>
            <VStack space={2} alignItems={'center'}>
              <Ionicons name="trash-outline" size={32} color={'#ac0909'} />
              <Heading size={'sm'}>
                Você está preste a deletar um ingrediente
              </Heading>
              <Box alignItems={'center'}>
                <Text fontWeight={'bold'} color={'#8d8d8d'}>
                  Isso ira deletar o ingrediente
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
                    setModalDeleteVisible(false);
                  }}
                >
                  Cancelar
                </Button>
                <Button
                  colorScheme={'warning'}
                  onPress={() => {
                    handleDeleteIngredient();
                  }}
                >
                  Confirmar
                </Button>
              </Button.Group>
            </Flex>
          </Modal.Body>
        </Modal.Content>
      </Modal>
      <Modal
        isOpen={modalQuantityVisible}
        onClose={() => {
          setModalQuantityVisible(false);
          handleUpdateQuantity();
        }}
      >
        <Modal.Content p={5}>
          <Modal.Body>
            <FormControl mt="3">
              <FormControl.Label>Nova quantidade</FormControl.Label>
              <HStack alignItems={'center'} space={2}>
                <Input
                  flex={1}
                  value={ingredient.quantity.toString()}
                  onChangeText={(e) =>
                    setIngredient({ ...ingredient, quantity: e })
                  }
                  keyboardType="numeric"
                />
                <Text flex={2}>{ingredient.unit?.unit}</Text>
              </HStack>
            </FormControl>
          </Modal.Body>
        </Modal.Content>
      </Modal>
    </>
  );
};

export default IngredientDetail;

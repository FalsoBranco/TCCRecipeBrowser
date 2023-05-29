import React, { useEffect, useState } from 'react';
import {
  Box,
  Image,
  Text,
  HStack,
  Center,
  Heading,
  VStack,
  Pressable,
} from 'native-base';
import Ionicons from '@expo/vector-icons/Ionicons';
import { useNavigation } from '@react-navigation/native';

const Card = ({ data, detail }) => {
  const navigation = useNavigation();
  const [item, setItem] = useState(data);

  function handleIncreaseQuantity() {
    setItem((state) => ({ ...state, quantity: state.quantity + 1 }));
  }
  function handleDecreaseQuantity() {
    if (item.quantity === 0) {
      return;
    }
    setItem((state) => ({ ...state, quantity: state.quantity - 1 }));
  }
  function handleDetail(id) {
    navigation.navigate(detail, { params: { itemId: id } });
  }

  return (
    <Center my="2" mx="4" flex="1">
      <Box
        borderColor="gray.700"
        borderWidth="1"
        w="full"
        h="32"
        rounded="lg"
        overflow="hidden"
      >
        <HStack space="2" m="2" flex="1">
          <Pressable flex="2" onPress={() => handleDetail(item.id)}>
            <HStack space="2" flex="1">
              <Box flex="1" w="full">
                <Image
                  size="full"
                  source={{
                    uri: 'https://placehold.co/400.png',
                  }}
                  alt="image"
                />
                {item.expired_date ? (
                  <Center
                    bg={item.days_to_expires < 10 ? 'red.600' : 'violet.500'}
                    rounded={'full'}
                    _text={{
                      color: 'warmGray.50',
                      fontWeight: '700',
                      fontSize: 'xs',
                    }}
                    position="absolute"
                    top={0}
                    px="3"
                    py="1.5"
                  >
                    {item.days_to_expires}
                  </Center>
                ) : null}
              </Box>
              <Heading flex="2" size="md" ml="-1">
                {item.title}
              </Heading>
            </HStack>
          </Pressable>

          {item.quantity >= 0 ? (
            <VStack alignItems={'center'} justifyContent={'center'}>
              <Pressable onPress={() => handleIncreaseQuantity()}>
                <Ionicons name="add-outline" size={32} />
              </Pressable>
              <Text>
                {item.quantity} {item.unit.unit}
              </Text>
              <Pressable onPress={() => handleDecreaseQuantity()}>
                <Ionicons name="remove-outline" size={32} />
              </Pressable>
            </VStack>
          ) : null}
        </HStack>
      </Box>
    </Center>
  );
};

export default Card;

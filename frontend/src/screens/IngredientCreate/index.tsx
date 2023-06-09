import React, { useState } from 'react';
import {
  FormControl,
  Input,
  VStack,
  Button,
  Center,
  Text,
  Box,
  Heading,
  Pressable,
  TextArea,
  ScrollView,
} from 'native-base';
import { Controller, useForm } from 'react-hook-form';
import { DateTimePickerAndroid } from '@react-native-community/datetimepicker';
import ingredientService from '@/services/IngredientService';
import { useNavigation } from '@react-navigation/native';

const IngredientCreate = () => {
  const navigation = useNavigation();
  const [date, setDate] = useState(new Date());

  const onChange = (event, selectedDate) => {
    const currentDate = selectedDate;
    setDate(currentDate);
  };

  const showMode = (currentMode) => {
    DateTimePickerAndroid.open({
      value: date,
      onChange,
      mode: currentMode,
      is24Hour: true,
    });
  };

  const showDatepicker = (onChange, value) => {
    showMode('date');
  };

  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm();
  // } = useForm<SignInFormType>({ resolver: zodResolver(SignInFormSchema) });
  async function onSubmitForm(data) {
    const ingredientData = {
      ingredient: {
        title: data.title,
        summary: data.summary,
        quantity: data.quantity,
        unit: data.unit,
        expired_date: date.toISOString().split('T')[0],
      },
    };
    const ingredient = await ingredientService.create(ingredientData);
    navigation.navigate('Ingredients');
  }

  return (
    <ScrollView>
      <Center h="100%">
        <Box safeArea p="2" py="8" w="90%" maxW="290">
          <Heading
            size="lg"
            fontWeight="600"
            color="black"
            _dark={{
              color: 'warmGray.50',
            }}
          >
            Novo Ingrediente
          </Heading>
          <VStack space={3} mt="5">
            <Controller
              name="title"
              control={control}
              render={({ field: { onChange, onBlur, value } }) => (
                <FormControl isRequired>
                  <FormControl.Label
                    _text={{
                      bold: true,
                    }}
                  >
                    Ingrediente
                  </FormControl.Label>
                  <Input
                    placeholder="Nome do Ingrediente"
                    onChangeText={onChange}
                    onBlur={onBlur}
                    value={value}
                  />
                </FormControl>
              )}
            />
            <Controller
              name="quantity"
              control={control}
              render={({ field: { onChange, onBlur, value } }) => (
                <FormControl isRequired>
                  <FormControl.Label
                    _text={{
                      bold: true,
                    }}
                  >
                    Quantidade
                  </FormControl.Label>
                  <Input
                    placeholder="Quantidade"
                    onChangeText={onChange}
                    onBlur={onBlur}
                    keyboardType="numeric"
                    value={value}
                  />
                </FormControl>
              )}
            />
            <Controller
              name="unit"
              control={control}
              render={({ field: { onChange, onBlur, value } }) => (
                <FormControl isRequired>
                  <FormControl.Label
                    _text={{
                      bold: true,
                    }}
                  >
                    Tipo da Unidade
                  </FormControl.Label>
                  <Input
                    placeholder="Unidade (Kg, L, Unit.)"
                    onChangeText={onChange}
                    onBlur={onBlur}
                    value={value}
                  />
                </FormControl>
              )}
            />
            <FormControl isRequired>
              <FormControl.Label
                _text={{
                  bold: true,
                }}
              >
                Data de Validade
              </FormControl.Label>
              <Pressable onPress={showDatepicker}>
                <Text>{date.toLocaleDateString('pt-BR')}</Text>
              </Pressable>
            </FormControl>
            <Controller
              name="summary"
              control={control}
              render={({ field: { onChange, onBlur, value } }) => (
                <FormControl isRequired>
                  <FormControl.Label
                    _text={{
                      bold: true,
                    }}
                  >
                    Descrição
                  </FormControl.Label>
                  <TextArea
                    autoCompleteType={true}
                    maxW="300"
                    h={32}
                    onChangeText={onChange}
                    onBlur={onBlur}
                    value={value}
                  />
                </FormControl>
              )}
            />
            <Button
              mt="2"
              colorScheme="indigo"
              onPress={handleSubmit(onSubmitForm)}
            >
              Enviar
            </Button>
          </VStack>
        </Box>
      </Center>
    </ScrollView>
  );
};

export default IngredientCreate;

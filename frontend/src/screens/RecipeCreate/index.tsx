import React, { useState } from 'react';
import {
  FormControl,
  Input,
  VStack,
  Button,
  Center,
  Box,
  Heading,
  TextArea,
} from 'native-base';
import { Controller, useForm } from 'react-hook-form';
import { DateTimePickerAndroid } from '@react-native-community/datetimepicker';
import RecipeService from '@/services/RecipeService';

const RecipeCreate = () => {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm();
  // } = useForm<SignInFormType>({ resolver: zodResolver(SignInFormSchema) });
  async function onSubmitForm(data) {
    const recipeData = {
      recipe: {
        title: data.title,
        summary: data.summary,
        amounts: data.amounts,
        instructions: data.instructions,
        unit: data.unit,
      },
    };
    await RecipeService.create(recipeData);
  }

  return (
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
          Nova Receita
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
                  Nome dda Receitas
                </FormControl.Label>
                <Input
                  placeholder="John"
                  onChangeText={onChange}
                  onBlur={onBlur}
                  value={value}
                />
              </FormControl>
            )}
          />
          <Controller
            name="amounts"
            control={control}
            render={({ field: { onChange, onBlur, value } }) => (
              <FormControl isRequired>
                <FormControl.Label
                  _text={{
                    bold: true,
                  }}
                >
                  Quantidade de Porções
                </FormControl.Label>
                <Input
                  placeholder="John"
                  onChangeText={(text) => onChange(parseInt(text))}
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
                  placeholder="John"
                  onChangeText={onChange}
                  onBlur={onBlur}
                  value={value}
                />
              </FormControl>
            )}
          />
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
          <Controller
            name="instructions"
            control={control}
            render={({ field: { onChange, onBlur, value } }) => (
              <FormControl isRequired>
                <FormControl.Label
                  _text={{
                    bold: true,
                  }}
                >
                  Instruções
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
  );
};

export default RecipeCreate;

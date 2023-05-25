import { Center, Box, Heading, VStack, Link, Button } from 'native-base';
import { useForm, Controller } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-community/async-storage';
import CustomInput from '@/components/Input';
import * as z from 'zod';
import AuthService from '@/services/AuthService';

const SignInFormSchema = z.object({
  username: z.string({
    required_error: 'O campo usuário é obrigatório',
  }),
  password: z.string({
    required_error: 'O campo Senha é obrigatório',
  }),
  // .min(8, 'Senha precisa conter mais de 8 dígitos'),
});

type SignInFormType = z.infer<typeof SignInFormSchema>;

const SignIn = () => {
  const navigation = useNavigation();

  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm<SignInFormType>({ resolver: zodResolver(SignInFormSchema) });
  async function onSubmitForm(data: SignInFormType) {
    let user = await AuthService.login(data);
    if (user) {
      await AsyncStorage.setItem('user', JSON.stringify(user));

      navigation.reset({ routes: [{ name: 'Preload' }] });
    }
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
          Bem Vindo
        </Heading>
        <VStack space={3} mt="5">
          <Controller
            name="username"
            control={control}
            render={({ field: { onChange, onBlur, value } }) => (
              <CustomInput
                labelName="Usuario"
                onBlur={onBlur}
                onChangeText={onChange}
                value={value}
                type="text"
                errorMessage={errors.username?.message}
              />
            )}
          />
          <Controller
            name="password"
            control={control}
            render={({ field: { onChange, onBlur, value } }) => (
              <CustomInput
                labelName="Senha"
                onBlur={onBlur}
                onChangeText={onChange}
                value={value}
                type="password"
                errorMessage={errors.password?.message}
              />
            )}
          />
          <Link
            _text={{
              fontSize: 'xs',
              fontWeight: '500',
              color: 'indigo.500',
            }}
            alignSelf="flex-end"
            mt="1"
          >
            Esqueceu a senha?
          </Link>
          <Button
            mt="2"
            colorScheme="indigo"
            onPress={handleSubmit(onSubmitForm)}
          >
            Entrar
          </Button>
        </VStack>
      </Box>
    </Center>
  );
};

export default SignIn;

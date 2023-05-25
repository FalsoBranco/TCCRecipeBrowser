import React, { useEffect } from 'react';
import { Center, Text, Pressable } from 'native-base';
import { useNavigation } from '@react-navigation/native';
import AsyncStorage from '@react-native-community/async-storage';
const SignIn = () => {
  const navigation = useNavigation();

  const checkTokenInStorage = async () => {
    const user = await AsyncStorage.getItem('user', (err, result) =>
      JSON.parse(result)
    );

    if (user) {
      navigation.reset({ routes: [{ name: 'MainApp' }] });
    } else {
      navigation.reset({ routes: [{ name: 'SignIn' }] });
    }
  };

  useEffect(() => {
    checkTokenInStorage();
  }, []);

  return (
    <Center
      flex={1}
      alignItems={'center'}
      flexDirection={'row'}
      justifyContent={'center'}
      paddingX={4}
    >
      <Pressable
        flex={1}
        bgColor="indigo.500"
        height={'10'}
        alignItems="center"
        justifyContent="center"
        onPress={() => navigation.navigate('SignIn')}
      >
        <Text color="black">Sign In</Text>
      </Pressable>
    </Center>
  );
};

export default SignIn;

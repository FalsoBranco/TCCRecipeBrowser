import {
  DrawerContentComponentProps,
  DrawerContentScrollView,
} from '@react-navigation/drawer';
import { Box, Button, Divider, HStack, Image, Text, VStack } from 'native-base';
import CustomDrawerItem from '@/components/CustomDrawer/CustomDrawerItem';
import AsyncStorage from '@react-native-community/async-storage';
import { useEffect, useState } from 'react';
import LogoutModal from '../LogoutModal';

async function resetStore() {
  await AsyncStorage.clear();
}

interface DrawerContentProps extends DrawerContentComponentProps {}

export default function CustomDrawerContent(props: DrawerContentProps) {
  const [user, setUser] = useState();
  useEffect(() => {
    async function loadStorageData() {
      const storagedUser = await AsyncStorage.getItem('user');

      if (storagedUser) {
        setUser(JSON.parse(storagedUser).user);
      }
    }
    loadStorageData();
  }, []);
  return (
    <DrawerContentScrollView {...props} contentContainerStyle={{ flex: 1 }}>
      <Box flex="1" justifyContent="space-between">
        <HStack justifyContent={'space-between'}>
          <VStack space="6">
            {/* UserInfo */}
            <Box px="5" py="3">
              <Image
                source={{
                  uri: user?.image
                    ? user?.image
                    : 'https://randomuser.me/api/portraits/men/1.jpg',
                }}
                alt={`${user?.username} portrait`}
                size="md"
              />
              <Text fontSize="14" mt="1" color="gray.500" fontWeight="500">
                {user?.username}
              </Text>
            </Box>
            {/* Routers */}
            <VStack divider={<Divider />} space="4">
              <VStack>
                {props.state.routeNames.map((name, index) => (
                  <CustomDrawerItem
                    key={name}
                    px="5"
                    py="3"
                    rounded="md"
                    bg={
                      index === props.state.index
                        ? 'rgba(6, 182, 212, 0.1)'
                        : 'transparent'
                    }
                    index={index}
                    name={name}
                    props={props}
                  />
                ))}
              </VStack>
            </VStack>
          </VStack>
          <LogoutModal />
        </HStack>
        {/* Socials */}
      </Box>
    </DrawerContentScrollView>
  );
}

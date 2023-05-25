import { useState, useRef } from 'react';
import {
  View,
  Text,
  Pressable,
  Modal,
  Button,
  Heading,
  VStack,
  Box,
  HStack,
  Center,
  Flex,
} from 'native-base';
import Ionicons from '@expo/vector-icons/Ionicons';
import AuthService from '@/services/AuthService';
import { useNavigation } from '@react-navigation/native';

const LogoutModal = () => {
  const navigation = useNavigation();
  const [modalVisible, setModalVisible] = useState(false);
  const initialRef = useRef(null);
  const finalRef = useRef(null);

  async function handleLogout() {
    await AuthService.logout(navigation);
    setModalVisible(false);
  }
  return (
    <View>
      {/* Button to open the logout popup */}
      <Pressable
        padding={2}
        margin={1}
        onPress={() => {
          setModalVisible(!modalVisible);
        }}
      >
        <Ionicons name="log-out-outline" size={32} />
      </Pressable>
      {/* Logout popup */}
      <Modal
        isOpen={modalVisible}
        onClose={() => setModalVisible(false)}
        initialFocusRef={initialRef}
        finalFocusRef={finalRef}
      >
        <Modal.Content>
          <Modal.Body>
            <HStack>
              <Center>
                <Box rounded={'full'} bg={'red.200'} p={2} mr={2}>
                  <Ionicons name="warning-outline" color={'red'} size={24} />
                </Box>
              </Center>
              <VStack>
                <Heading>Sair?</Heading>
                <Text>Você tem certeza que deseja sair?</Text>
              </VStack>
            </HStack>
          </Modal.Body>
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
                onPress={() => {
                  handleLogout();
                }}
              >
                Confirmar
              </Button>
            </Button.Group>
          </Flex>
        </Modal.Content>
      </Modal>
    </View>
  );
};

export default LogoutModal;

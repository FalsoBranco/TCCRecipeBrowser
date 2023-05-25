import { createDrawerNavigator } from '@react-navigation/drawer';
import { Box, Button, Pressable } from 'native-base';
import Ionicons from '@expo/vector-icons/Ionicons';

import Ingredients from '@/screens/Ingredients';
import Recipes from '@/screens/Recipes';
import Settings from '@/screens/Settings';

import CustomDrawerContent from '@/components/CustomDrawer';
import { useNavigation } from '@react-navigation/native';

const { Screen, Navigator } = createDrawerNavigator();

const MainAppDrawer = () => {
  const navigation = useNavigation();
  return (
    <Box safeArea flex="1">
      <Navigator drawerContent={(props) => <CustomDrawerContent {...props} />}>
        <Screen
          name="Ingredients"
          component={Ingredients}
          options={{
            headerRight: () => (
              <Pressable
                mr={4}
                onPress={() => navigation.navigate('CreateIngredient')}
                color="#fff"
              >
                <Ionicons name="create-outline" size={24} />
              </Pressable>
            ),
          }}
        />
        <Screen name="Recipes" component={Recipes} />
        <Screen name="Settings" component={Settings} />
      </Navigator>
    </Box>
  );
};

export default MainAppDrawer;

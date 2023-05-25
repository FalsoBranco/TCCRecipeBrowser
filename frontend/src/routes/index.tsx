import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import RootStack from './rootStack';
const Routes = () => {
  return (
    <NavigationContainer>
      <RootStack />
    </NavigationContainer>
  );
};

export default Routes;

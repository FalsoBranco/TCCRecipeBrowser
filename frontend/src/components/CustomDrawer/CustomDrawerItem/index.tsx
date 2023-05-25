import React from 'react';
import { Pressable, IPressableProps, Text } from 'native-base';
import { DrawerContentComponentProps } from '@react-navigation/drawer';

interface DrawerItemProps extends IPressableProps {
  name: string;
  index: number;
  props: DrawerContentComponentProps;
}

const CustomDrawerItem = ({ index, name, props, ...rest }: DrawerItemProps) => {
  return (
    <Pressable
      {...rest}
      onPress={(event) => {
        props.navigation.navigate(name);
      }}
    >
      <Text
        fontWeight="500"
        color={index === props.state.index ? 'primary.500' : 'gray.700'}
      >
        {name}
      </Text>
    </Pressable>
  );
};

export default CustomDrawerItem;

import React, { useEffect, useState } from 'react';
import { Box, FlatList, Text, View } from 'native-base';

import Card from '@/components/Card';
import IngredientService from '@/services/IngredientService';
import { RefreshControl } from 'react-native-gesture-handler';

const Ingredients = () => {
  const [refreshing, setRefreshing] = useState(false);
  const [data, setData] = useState();

  async function loadIngredients() {
    const response = await IngredientService.getAll();
    if (!response) {
      return <View>Alo</View>;
    }
    setData(response);
  }
  const onRefreshing = () => {
    loadIngredients();
  };

  useEffect(() => {
    loadIngredients();
  }, []);

  return (
    <Box safeArea flex="1">
      <FlatList
        showsVerticalScrollIndicator={false}
        flex={1}
        data={data}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => <Card data={item} />}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={() => onRefreshing()}
          />
        }
      />
    </Box>
  );
};

export default Ingredients;

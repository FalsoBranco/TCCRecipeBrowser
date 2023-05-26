import React, { useEffect, useState } from 'react';
import { Box, FlatList, Text, View } from 'native-base';
import { RefreshControl } from 'react-native-gesture-handler';
import Card from '@/components/Card';
import RecipeService from '@/services/RecipeService';

const Recipes = () => {
  const [data, setData] = useState();
  const [refreshing, setRefreshing] = useState(false);
  async function loadRecipes() {
    const response = await RecipeService.getAll();
    if (!response) {
      return <View>Alo</View>;
    }
    setData(response);
  }
  const onRefreshing = () => {
    loadRecipes();
  };
  useEffect(() => {
    loadRecipes();
  }, []);

  return (
    <Box safeArea flex="1">
      <FlatList
        showsVerticalScrollIndicator={false}
        flex={1}
        data={data}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => <Card data={item} detail={'DetailRecipe'} />}
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

export default Recipes;

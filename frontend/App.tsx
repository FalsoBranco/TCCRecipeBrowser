import { NativeBaseProvider, StatusBar, extendTheme, Text } from 'native-base';
import theme from '@/theme';
import Routes from '@/routes';
import 'react-native-gesture-handler';

export default function App() {
  return (
    <NativeBaseProvider theme={theme}>
      <StatusBar />
      <Routes />
    </NativeBaseProvider>
  );
}

import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import LaundryDone from './components/LaundryDone.component';

export default function App() {
  return (
    <View style={styles.container}>
      <Image style={styles.mainImg} source={{uri: 'https://fontmeme.com/permalink/200715/7ed6c1eb5b70001428db324af51b5993.png'}}/>
      <LaundryDone></LaundryDone>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#BDBDBD',
    alignItems: 'center',
    justifyContent: 'center',
  },
  mainImg: {
    width: 360, 
    height: 360, 
    resizeMode: 'contain',
    position: 'absolute',
    top: 0
  }
});

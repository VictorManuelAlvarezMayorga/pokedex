import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput,
  Pressable, Image
} from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
     <View> {/*container-image */}
      <Image source={{uri: "https://pngimg.com/d/pokeball_PNG7.png"}}
      width={200}
      height = {200}
      />
     </View>{/*container-image */}
     <Text style={styles.title}>Iniciar sesion</Text> {/* title */}
     <Text style={styles.label}>Correo:</Text> {/* label */}
     <TextInput style={styles.input}/>
     <Text style={styles.label}>Contraseña:</Text> {/* label */}
     <TextInput style={styles.input}/>
     <Pressable >
     <Text style={styles.send.textButton}>Enviar</Text>
     </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize:24,
    fontWeight: 'bold'
  },
  label: {
    fontSize: 15,
    fontWeight: 'bold'
  },
  input:{
    borderRadius: 10,
    fontSize: 15,
    borderColor: 'black',
    width: 'auto',
    borderWidth: 2
  },
  send: {
    backgroundColor: 'red',
    width: 'auto',
    height: 'auto',
    borderRadius:10,
    marginTop: 15,
    alignItems:'center',
    textButton:{
      color: 'white',
      fontWeight: 'bold',
      fontSize: 20,
    }
  },
  containerFooter: {
    justifyContent: 'space-between',
    alignItems: 'center',
    texts:{
      fontSize: 20,
      margin: 5
    }
  }
});

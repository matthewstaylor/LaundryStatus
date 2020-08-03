import React, {Component, useEffect} from 'react';
import { View, Text, StyleSheet } from 'react-native'

export default class LaundryDone extends Component {
    endpoint: string ='http://ec2-52-14-234-1.us-east-2.compute.amazonaws.com/laundry';



    state = {
        data: {
            laundry_status: '',
            time_posted: '',
            color: '#0e3d56'
        }
    }
    
    interval: any;

    componentDidMount() {
        this.getLaundryDone();
        this.interval = setInterval(
            () => this.getLaundryDone(),
            15000
        );
    }

    getLaundryDone() {
      fetch(this.endpoint)
          .then((response) => response.json())
          .then((responseJson) => {
              this.setState({data: responseJson})
              console.log(responseJson)
          })
          .catch((error) => {
            console.error(error);
          });   
    }

    render() {
        return(
            <View style={styles.container}>
                <View style={[styles.circle, {backgroundColor: this.state.data.color}]}/>
                {
                    <View>
                        <Text style={styles.status}>{this.state.data.laundry_status}</Text>
                        <Text style={styles.status}>{this.state.data.time_posted.substring(5, this.state.data.time_posted.length-3)}</Text>
                    </View>
                }
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 0.2,
        paddingRight: 15,
        paddingLeft: 15,
        backgroundColor: '#EBEDF3',
        alignItems: 'center',
        justifyContent: 'center',
        borderWidth: 3,
        borderColor: '#6699CC'
    },
    status: {
        fontSize: 38,
        textAlign: 'center',
        color: '#0e3d56'
    },
    circle: {
        width: 15,
        height: 15,
        borderRadius: 15 / 2,
        position: 'absolute',
        top: 10,
        left: 10
    },
});
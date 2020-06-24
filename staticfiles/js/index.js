import React, {Component} from 'react';
import ReactDOM from 'react-dom';


class DatosPregunta extends Component{
    render(){
        /*obtenemos los datos JSON para recorrerlos*/
        const datos = window.props;
        console.log(datos);
        return (
            <div>
                {datos.map(dato => <ComponentePregunta
                texto={dato.texto} categoria={dato.categoria__nombre}/>)}
            </div>
        )
    }
}

class ComponentePregunta extends Component{
    render(){
        return(
            <ul>
                <li>{this.props.texto}-{this.props.categoria}</li>
            </ul>
        )
    }
}


ReactDOM.render(
    <DatosPregunta/>, window.react_mount,
);
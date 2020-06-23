import React from 'react';
import Card from "./Card";

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      "cards": [{"suit": "diamond", "face_value": "3"}, {"suit": "heart", "face_value": "3"}]
    };
  }

  render() {
    return (
      <Card 
        cards={this.state.cards}
      />
    );
  }
}

export default App;


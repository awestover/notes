import React from 'react';
import './Card.css';

class Card extends React.Component {
  constructor(props){
    super(props);
    this.state = {};
  }

  render() {
    const cards = this.props.cards.map((card, index) => {
      return (
        <div key={index} className="playingcard">
          <h1>suit: {card.suit}</h1>
          <h1>face_value: {card.face_value}</h1>
        </div>
      );
    });

    return (
      <div>
        {cards}
      </div>
    );
  }
}

export default Card;


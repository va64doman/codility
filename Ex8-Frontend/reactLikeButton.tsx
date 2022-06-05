import * as React from "react";
import { render } from "react-dom";
import "./reactLikeStyle.css";

class Buttons extends React.Component {

  state = {
    hasLiked: false,
    like: 100,
  }

  handleLike = () => {
    this.setState({
        hasLiked: !this.state.hasLiked
      });
  }

  render() {
    const { hasLiked } = this.state;
    const classLikeButton = `like-button ${hasLiked ? 'liked': ''}`;

    return (
      <div>
        <button className={classLikeButton} onClick={this.handleLike}>
          Like |
          <span className="likes-counter">
            {this.state.hasLiked ? this.state.like + 1 : this.state.like}
          </span>
        </button>
      </div>
    );
  }
}

function App() {
  return <Buttons />;
}

const rootElement = document.getElementById("root");
render(<App />, rootElement);
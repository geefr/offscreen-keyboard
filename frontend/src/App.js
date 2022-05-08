import './App.css';

function apiPressKey(k) {
  return fetch('/keypress?key=' + k, {method: 'PUT'});
}

function App() {
  return (
    <div className="numpad-container">
      <button class="numpad-button"></button>
      <button class="numpad-button" onClick={() => {apiPressKey('/')}}>/</button>
      <button class="numpad-button" onClick={() => {apiPressKey('*')}}>*</button>
      <button class="numpad-button" onClick={() => {apiPressKey('-')}}>-</button>
      {/* <div class="numpad-row"> */}
        <button class="numpad-button" onClick={() => {apiPressKey('num7')}}>7</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num8')}}>8</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num9')}}>9</button>
        <button class="numpad-button" onClick={() => {apiPressKey('+')}}>+</button>
      {/* </div> */}
      {/* <div class="numpad-row"> */}
        <button class="numpad-button" onClick={() => {apiPressKey('num4')}}>4</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num5')}}>5</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num6')}}>6</button>
        <button class="numpad-button"></button>
      {/* </div> */}
      {/* <div class="numpad-row"> */}
        <button class="numpad-button" onClick={() => {apiPressKey('num1')}}>1</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num2')}}>2</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num3')}}>3</button>
        <button class="numpad-button"></button>
      {/* </div> */}
      <button class="numpad-button"></button>
        <button class="numpad-button" onClick={() => {apiPressKey('num0')}}>0</button>
        <button class="numpad-button" onClick={() => {apiPressKey('.')}}>.</button>
        <button class="numpad-button" onClick={() => {apiPressKey('enter')}}>⏎</button>
    </div>
  );
}

export default App;

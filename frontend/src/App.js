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
        <button class="numpad-button" onClick={() => {apiPressKey('num 7')}}>7</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 8')}}>8</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 9')}}>9</button>
        <button class="numpad-button" onClick={() => {apiPressKey('+')}}>+</button>
      {/* </div> */}
      {/* <div class="numpad-row"> */}
        <button class="numpad-button" onClick={() => {apiPressKey('num 4')}}>4</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 5')}}>5</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 6')}}>6</button>
        <button class="numpad-button"></button>
      {/* </div> */}
      {/* <div class="numpad-row"> */}
        <button class="numpad-button" onClick={() => {apiPressKey('num 1')}}>1</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 2')}}>2</button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 3')}}>3</button>
        <button class="numpad-button" onClick={() => {apiPressKey('backspace')}}>⌫</button>
      {/* </div> */}
      <button class="numpad-button"></button>
        <button class="numpad-button" onClick={() => {apiPressKey('num 0')}}>0</button>
        <button class="numpad-button" onClick={() => {apiPressKey('.')}}>.</button>
        <button class="numpad-button" onClick={() => {apiPressKey('enter')}}>⏎</button>
    </div>
  );
}

export default App;

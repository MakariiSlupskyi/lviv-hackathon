import { WebSocketDisplay } from "./WebSocketDisplay";

function App() {
  return (
    <div className="App flex w-full h-screen">
      <div className="m-auto">
        <WebSocketDisplay stream_id="11ce5d48-e2d7-41d1-8982-276ea3b361ae" />
      </div>
    </div>
  );
}

export default App;

import "./App.css";
import ArtistaCover from "./components/artista/ArtistaCover";
import BottomPlayer from "./components/bottom-player/BottomPlayer";

function App() {
  return (
    <>
      <ArtistaCover artistId={1} />
      <BottomPlayer />
    </>
  );
}

export default App;

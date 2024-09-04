import { Song } from "../../types/types";
import "./index.css";

export default function SongsRow({ title, played_times, inList }: Song) {
  return (
    <div className="songs-row">
      <div className="left-side">
        <h2>{inList}</h2>
        <img
          src="https://i.scdn.co/image/ab67616d00001e02b657fbb27b17e7bd4691c2b2"
          alt="song-image"
        />
        <a href="/">{title}</a>
      </div>

      <div className="right-side">
        <p className="times-played">{played_times}</p>
        <button className="check-button" />
        <span>3:01</span>
      </div>
    </div>
  );
}

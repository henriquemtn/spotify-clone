import { useEffect, useState } from "react";
import "./index.css";
import VerifiedIcon from "../../assets/verified-icon.png";
import { Artist, Song } from "../../types/types";
import { api } from "../../lib/axios";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import SongsRow from "../songs/SongsRow";

export default function ArtistaCover({ artistId }: { artistId: number }) {
  const [artist, setArtist] = useState<Artist | null>();

  // Garantir que seja uma função assincrona
  useEffect(() => {
    const fetchArtist = async () => {
      try {
        const response = await api.get<Artist>(`/api/artists/${artistId}/`);
        setArtist(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchArtist();
  }, [artistId]);

  if (!artist) return <p>No artist data available.</p>;

  return (
    <div className="container-artists">
      <div
        className="artist-banner"
        style={{ backgroundImage: `url(${artist.banner})` }}
      >
        <div className="artist-info">
          {artist.isVerified && (
            <div className="verified-artist">
              <img
                className="verified-icon"
                src={VerifiedIcon}
                alt="Verified Icon"
              />
              <p>Artista verificado</p>
            </div>
          )}
          <h2 className="artist-name">{artist.name}</h2>
          <p className="artist-listeners">16.367.365 ouvintes mensais</p>
        </div>
      </div>
      <div className="artist-body">
        <div className="actions">
          <button className="play-button">
            <PlayArrowIcon sx={{ width: 32, height: 32 }} />
          </button>
          <button className="following-button">Seguindo</button>
          <button className="dots-button">...</button>
        </div>

        <div className="songs-container">
          <h3>Populares</h3>
          <div className="table-songs">
            {artist.songs && artist.songs.length > 0 ? (
              artist.songs.map((song: Song, index: number) => (
                <SongsRow
                  key={song.id}
                  inList={index + 1}
                  id={song.id}
                  title={song.title}
                  played_times={song.played_times}
                  artist={song.artist}
                  audio_file={song.audio_file}
                />
              ))
            ) : (
              <p>No songs available.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

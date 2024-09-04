import { useEffect, useState } from "react";
import "./index.css";
import VerifiedIcon from "../../assets/verified-icon.png";
import { Artist } from "../../types/types";
import { api } from "../../lib/axios";

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
    </div>
  );
}

export interface Song {
    id: number;
    title: string;
    artist: number;
    audio_file: string;
    played_times: number;
  }
  
export interface Artist {
    id: number;
    name: string;
    banner: string;
    isVerified: boolean;
    songs: Song[];
    genre: string;
    album_ids: number[];
  }
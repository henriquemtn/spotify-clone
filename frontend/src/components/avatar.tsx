import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';

export default function ImageAvatars() {
  return (
    <Stack direction="row" spacing={2}>
      <Avatar alt="Henrique Silveira" src="https://avatars.githubusercontent.com/u/92762031?v=4" />
    </Stack>
  );
}

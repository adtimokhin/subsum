import { Box, Flex, Spacer, Heading } from '@chakra-ui/react';
import ProfileMenu from './ProfileMenu';


export default function Navbar() {
  return (
    <Box bg="blue.500" px={4} py={3} shadow="md">
      <Flex align="center">
        {/* Logo */}
        <Heading as="h1" size="lg" color="white">
          Subsum
        </Heading>
        <Spacer />
        {/* Profile Dropdown */}
        <ProfileMenu />
      </Flex>
    </Box>
  );
}

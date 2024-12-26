import { Avatar, AvatarGroup } from "@/components/ui/avatar";
import {
  MenuContent,
  MenuItem,
  MenuRoot,
  MenuTrigger,
} from "@/components/ui/menu";
import { Button } from "@chakra-ui/react";

export default function ProfileMenu() {
  const handleModifyAccount = () => {
    console.log("Modify Account clicked");
    // Add navigation logic here
  };

  const handleLogout = () => {
    console.log("Logout clicked");
    // Add logout logic here
  };

  const handleDeleteAccount = () => {
    console.log("Delete Account clicked");
    // Add delete account logic here
  };

  return (
    <MenuRoot>
      <MenuTrigger asChild>
        <AvatarGroup>
          <Avatar variant="solid" name="Aleksandr Timokhin" />
        </AvatarGroup>
      </MenuTrigger>
      <MenuContent>
        <MenuItem value="rename">Edit Profile</MenuItem>
        <MenuItem
          value="delete"
          color="fg.error"
          _hover={{ bg: "bg.error", color: "fg.error" }}
        >
          Delete Account
        </MenuItem>
      </MenuContent>
    </MenuRoot>
  );
}

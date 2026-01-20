import { Controller, Get } from '@nestjs/common';
import { UserService } from './user.service';

@Controller('profile')
export class ProfileController {
  constructor(private readonly userService: UserService) {}

  @Get()
  getProfile(): string {
    return 'This will return the user profile';
  }
}

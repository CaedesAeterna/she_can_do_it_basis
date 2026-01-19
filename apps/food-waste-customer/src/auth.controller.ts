import { Controller, Get } from '@nestjs/common';
import { UserService } from './user.service';

@Controller('auth')
export class AuthController {
  constructor(private readonly userService: UserService) {}

  @Get('login')
  login(): string {
    return 'This will be the login endpoint';
  }

  @Get('register')
  register(): string {
      return 'This will be the register endpoint';
  }
}

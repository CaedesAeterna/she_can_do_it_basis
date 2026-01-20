import { Module } from '@nestjs/common';
import { AuthController } from './controllers/auth.controller';
import { ProfileController } from './profile.controller';
import { UserService } from './user.service';

@Module({
  imports: [],
  controllers: [AuthController, ProfileController],
  providers: [UserService],
})
export class UserModule {}